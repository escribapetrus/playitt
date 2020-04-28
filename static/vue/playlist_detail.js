Vue.component('vtracklist', {
    props:['songs','title','artist','album'],
    delimiters: ['[[', ']]'],
    template: '<li>[[title]] <span>[[artist]] - [[album]]</span></li>'
})

var vueTracklist = new Vue({
    el: '#vue-playlist',
    component: ['vtracklist'],
    data: {
        songs: [
            {
            title: "The Drapery Falls",
            artist: "Opeth",
            album: "The Drapery Falls"
            },
            {
            title: "Nothing Else Matters",
            artist: "Metallica",
            album: "Metallica"
            },
            {
            title: "Stargazer",
            artist: "Rainbow",
            album: "Rising"
            },
            {
            title: "Money",
            artist: "Pink Floyd",
            album: "The Dark Side of the Moon"
            },
            {
            title: "Over the Hills and Far Away",
            artist: "Gary Moore",
            album: "Wild Frontier"
            },
            {
            title: "Gutter Ballet",
            artist: "Savatage",
            album: "Gutter Ballet"
            },
            {
            title: "Hallowed by thy name",
            artist: "Iron Maiden",
            album: "The number of the beast"
            },
            {
            title: "Sacrament of Wilderness",
            artist: "Nightwish",
            album: "Oceanborn"
            },
            {
            title: "Percées de Lumière",
            artist: "Alcest",
            album: "Écailles de Lune"
            }
        ],
    },
    methods: {
        getSongs: function() {
            fetch('/api/playlists/42').then((res) => console.log(res))
        }
    },
    delimiters: ['[[', ']]'],
})

