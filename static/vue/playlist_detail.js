Vue.component('vuetrack',{
    props: ['track'],
    template: '<span>[[track.title]]</span>',
    delimiters: ['[[', ']]'],
})

var vueTracklist = new Vue({
    el: '#vue-tracklist',
    data: {
        tracks: [
            {
            id: 41,
            title: "indie pop party",
            user_id: 7,
            description: "Wanna party? Wanna rock? I created this playlist as a dj set for an indie party in São Paulo. The idea is to merge new and old dance pop and indie rock.",
            date_created: "2020-04-22T23:56:44.819Z"
            },
            {
            id: 42,
            title: "acoustic folk",
            user_id: 7,
            description: "My selection of favourite acoustic songs, old and new.",
            date_created: "2020-04-23T00:12:27.796Z"
            },
            {
            id: 43,
            title: "guitar practice",
            user_id: 7,
            description: "These are my choices for practicing guitar: some blues licks, some minor and minor harmonic scales, some shred, mostly fun stuff.",
            date_created: "2020-04-23T00:25:05Z"
            },
            {
            id: 44,
            title: "listy list list",
            user_id: 8,
            description: "asdfasdf",
            date_created: "2020-04-23T16:23:49.631Z"
            }
            ],
    },
    methods: {
        refreshTracklist: function(){
            fetch('/api/playlists/').then(res => this.tracks = res.data)
        }
    },
    delimiters: ['[[', ']]'],
})
