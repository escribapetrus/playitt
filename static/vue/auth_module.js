var authPages = [
    {id: 1, name: "sign up", link: "/users/create/"},
    {id: 1, name: "log in", link: "/users/login/"},
]

var authModule = new Vue({
    el: "#auth-module",
    delimiters: ["[[", "]]"],
    data: {
        modal: ""
    },
    methods: {
        openAuthModal: function(link){
            console.log(link);
            this.modal = link
        },
        closeAuthModal: function(){
            this.modal = ""
        }
    }
})