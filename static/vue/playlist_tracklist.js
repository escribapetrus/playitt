Vue.component('vtracklist', {
    props:['title','artist','album'],
    delimiters: ['[[', ']]'],
    template: '<li>[[title]] <span>[[artist]] - [[album]]</span></li>'
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
                album:this.song.album
            }
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            axios.post(`${window.location.origin}${window.location.pathname}addsong/`, addData)
            .then(res => (this.$emit("addedsong")))
            .catch(err => (console.log(err)));
        }
    },
    data: () => ({song: {title:'',artist:'',album:''}}),
    template: `
    <div class="add-songs">
        <h3> Add new songs</h3>
        <form @submit.prevent="addSong">
            <input type="text" placeholder="title" v-model="song.title">
            <input type="text" placeholder="artist" v-model="song.artist">
            <input type="text" placeholder="album" v-model="song.album">
            <input type="submit" value="add">
        </form>
        </div>
    </div>        
    `
})

Vue.component('vplfavorite' ,{
    delimiters: ['[[',']]'],
    props: ['isfavorite'],
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
        <div class="playlist-edit">
            <i class="material-icons" v-if="isfavorite" @click="removeFavorite">remove_circle</i>
            <i class="material-icons" v-else @click="addToFavorites">stars</i>
            <span :message="message">
                [[message]]         
            </span>
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

