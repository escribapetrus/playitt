Vue.component('vtracklist', {
    props:['songs','iscreator','deleteurl'],
    delimiters: ['[[', ']]'],
    data: () => ({toggle: false, message:""}),
    methods: {
        removeTrack: function(songid) {
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            axios.post(`${window.location.origin}${window.location.pathname}removesong/${songid}`)
            .then(res => {
                console.log(res.data)
                this.message = "removed track from playlist";
                this.$emit("songremoved",res.data);
            })
            .catch(err => (console.log(err)))
        },
        deletePlaylist: function(songid) {
            return console.log('later')
            // axios.defaults.xsrfCookieName = 'csrftoken';
            // axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            // axios.get(`${window.location.origin}${window.location.pathname}delete/`)
            // .then(res => {
            //     window.location.href = res.data
            //     }
            // )
            // .catch(err => (console.log(err)))
        },
    },
    template: `
    <div>
    <div class="tracklist-header" v-if="iscreator">
        <i class="material-icons" @click="toggle = !toggle">text_fields</i>
        <a :href="deleteurl"><i class="material-icons">delete</i></a>
        <h3>playlist</h3>
    </div>
    <li v-for="(s, idx) in songs">
        <div class="track-info">
            [[s.title]] 
            <span v-if="s.album">[[s.artist]] - [[s.album]]</span>
            <span v-else="s.album">[[s.artist]]</span>
        </div>
        <i class="material-icons" v-show="toggle" @click="removeTrack(s.id)">clear</i>
    </li>
    </div>
    `
})

Vue.component('vpldescription',{
    props:['description','genres','url'],
    delimiters: ['[[',']]'],
    template: `
        <div class="description">
            <div class="tags">
                <h3 v-for="(g, idx) in genres ">
                    <a :href="[[url]] + [[g]]">[[g]]</a>
                </h3>
            </div>
            <p>[[description]]</p>
        </div>  
    `,
})

Vue.component('vsongadder',{
    delimiters: ['[[',']]'],
    props: {notfound: Boolean},
    methods: {
        addSong: function(){
            let addData = {
                title:this.song.title,
                artist:this.song.artist,
                custom:this.song.custom,
            }
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            axios.post(`${window.location.origin}${window.location.pathname}addsong/`, addData)
            .then(res => (this.$emit("addedsong", res.data)))
            .catch(err => (console.log(err)));
            this.song = {title:'',artist:'',}
        }
    },
    data: () => ({song: {title:'',artist:'', custom: false}}),
    template: `
    <div class="add-songs">
        <h3> Add new songs</h3>
        <h5 v-if="notfound">track not found, sorry.</h5>
        <form @submit.prevent="addSong">
            <label class="hide">title</label>
            <input type="text" placeholder="title" v-model="song.title">
            <label class="hide">artist</label>
            <input type="text" placeholder="artist" v-model="song.artist">
            <label>Didn't find your song in the library? Create a custom: </label>
            <input type="checkbox" v-model="song.custom">
            <input type="submit" value="add">
        </form>
        </div>
    </div>        
    `
})

Vue.component('vplfavorite' ,{
    delimiters: ['[[',']]'],
    props: {playlistid: Number},
    methods: {
        addToFavorites: function() {
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            axios.post(`${window.location.origin}/users/add-to-fav${window.location.pathname}`)
            .then(res => { this.message_ = "added to favorites" })
            .catch(err => (console.log(err)))
            .finally(() => this.checkFavorites())
        },
        removeFavorite: function() {
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            axios.post(`${window.location.origin}/users/remove-fav${window.location.pathname}`)
            .then(res => { this.message_ = "removed from favorites" })
            .catch(err => (console.log(err)))
            .finally(() => this.checkFavorites())
        },
        checkFavorites: function() {
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            axios.get(`${window.location.origin}/api/playlists/user-favorites`)
            .then(res => { this.userFavorites = res.data })
            .catch(err => (console.log(err)))
        },
        log: function() {
            console.log({playlist: this.playlistid, favs: this.userFavorites, isfav: this.isFavorite})
        }
    },
    computed: {
        isFavorite: function(){
            let filtered = this.userFavorites.filter(el => el.pk === this.playlistid);
            return filtered.length >= 1
        }
    },
    data() { return {userFavorites: []} },
    mounted(){ this.checkFavorites() },
    template: `
        <div class="tracklist-header">
            <i class="material-icons" v-if="isFavorite" @click="removeFavorite">remove_circle</i>
            <i class="material-icons" v-else @click="addToFavorites">stars</i>
            <span v-if="isFavorite">In your favorites!</span>
            <span v-else>Add to favorites?</span>
        </div>
    `
})



var vueTracklist = new Vue({
    el: '#vue-playlist',
    component: ['vtracklist','vpldescription','vplgenres','vsongadder','vplfavorite'],    
    delimiters: ['[[', ']]'],
    data: {
        playlistid: 0,
        songs: [],
        description: "",
        genres: [],
        notfound: false
    },
    methods: {
        getSongs: function(message) {
            if (message.success === false) {
                this.notfound = true;
            } else {
                axios.get(`${window.location.origin}/api${window.location.pathname}`)
                .then(res => {
                    this.playlistid = res.data[0].pk;
                    this.description = res.data[0].fields.description;
                    this.genres = res.data[0].fields.genres;
                    this.songs = res.data[0].fields.songs;
                    this.notfound = false;
                })
                .catch(err => (console.log(err)))
            }
        },
    },
    mounted() {
        this.getSongs({success: true})
    }
})

