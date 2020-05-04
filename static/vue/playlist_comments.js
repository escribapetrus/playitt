Vue.component('vcommentlist',{
    delimiters: ['[[',']]'],
    props: ['text','user','comment_date','url'],
    template:`
        <div class="comment">
            <div class="comment-header">
                <a :href="url"><h4>[[user]]</h4></a>
                <span>[[comment_date]]</span>
            </div>            
            <p>[[text]]</p>
        </div>
    `
})

Vue.component('vaddcomment',{
    delimiters: ['[[',']]'],
    data: () => ({comment: {text:""}}),
    methods: {
        addComment: function(){
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            axios.post(`${window.location.origin}/comments${window.location.pathname}`,{text:this.comment.text})
            .then(res => (this.$emit("addedcomment")))
            .catch(err => (console.log(err)));
        }
    },
    template:`
        <form @submit.prevent="addComment">
            <textarea placeholder="write your comment" v-model="comment.text"></textarea>
            <input class="input-submit" type="submit" value="submit">
        </form>
    `
})

var vueComments = new Vue({
    el: "#vue-comments",
    component: ['vcommentlist','vaddcomment'],
    delimiters: ['[[', ']]'],
    data: {
        comments: [],
    },
    methods: {
        getComments: function() {
            axios.get(`${window.location.origin}/api/comments${window.location.pathname}`)
            .then(res => (this.comments = res.data))
            .catch(err => console.log(err))
        }
    },
    mounted(){
        this.getComments();
    }
})