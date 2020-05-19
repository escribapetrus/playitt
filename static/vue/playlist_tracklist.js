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
                    console.log(res)
                    this.message = "removed track from playlist",
                    this.$emit("songremoved")
                }
            )
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
    <li v-for="s in songs" v-bind:key="s.title">
        <div class="track-info">
            [[s.title]] <span>[[s.artist]] - [[s.album]]</span>
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
                <h3 v-for="g in genres">
                    <a :href="[[url]] + [[g]]">[[g]]</a>
                </h3>
            </div>
            <p>[[description]]</p>
        </div>  
    `,
})

Vue.component('vsongadder',{
    delimiters: ['[[',']]'],
    methods: {
        addSong: function(){
            let addData = {
                title:this.song.title,
                artist:this.song.artist,
            }
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            axios.post(`${window.location.origin}${window.location.pathname}addsong/`, addData)
            .then(res => (this.$emit("addedsong")))
            .catch(err => (console.log(err)));
            this.song = {title:'',artist:'',}
        }
    },
    data: () => ({song: {title:'',artist:'',}}),
    template: `
    <div class="add-songs">
        <h3> Add new songs</h3>
        <form @submit.prevent="addSong">
            <label>title</label>
            <input type="text" placeholder="title" v-model="song.title">
            <label>artist</label>
            <input type="text" placeholder="artist" v-model="song.artist">
            <input type="submit" value="add">
        </form>
        </div>
    </div>        
    `
})

Vue.component('vplfavorite' ,{
    delimiters: ['[[',']]'],
    props: ['isfavorite','message'],
    data: () => ({message: ""}),
    methods: {
        addToFavorites: function() {
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            axios.post(`${window.location.origin}/users/add-to-fav${window.location.pathname}`)
            .then(res => {
                    console.log(res)
                    this.message = "added to favorites"
                }
            )
            .catch(err => (console.log(err)))
        },
        removeFavorite: function() {
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            axios.post(`${window.location.origin}/users/remove-fav${window.location.pathname}`)
            .then(res => {
                    console.log(res)
                    this.message = "removed from favorites"
                }
            )
            .catch(err => (console.log(err)))
        },
    },
    template: `
        <div class="tracklist-header">
            <i class="material-icons" v-if="isfavorite" @click="removeFavorite">remove_circle</i>
            <i class="material-icons" v-else @click="addToFavorites">stars</i>
            <h3>[[message]]</h3>
        </div>
    `
})

var vueTracklist = new Vue({
    el: '#vue-playlist',
    component: ['vtracklist','vpldescription','vplgenres','vsongadder','vplfavorite'],    
    delimiters: ['[[', ']]'],
    data: {
        songs: [],
        description: "",
        genres: [],
    },
    methods: {
        getSongs: function() {
            axios.get(`${window.location.origin}/api${window.location.pathname}`)
            .then(res => {
                this.songs = res.data[0].fields.songs
                this.description = res.data[0].fields.description
                this.genres = res.data[0].fields.genres
            })
            .catch(err => (console.log(err)))
        },
    },
    mounted() {
        this.getSongs()
    }
})

