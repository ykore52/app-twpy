let app = new Vue({
    el: '#tweetApp',
    data: {
        searchWord: ""
    },
    methods: {
        search: function() {
            let searchParams = {
                'q': this.searchWord === "" ? "twitter": this.searchWord,
                'result_type': 'recent',
                'count': 10
            }

            let params = new URLSearchParams(searchParams)
            this.get_ajax(params, "tweets")
        },

        get_ajax: function(url, name) {
            return axios.get("/api/search?" + url)
            .then((res) => {
                Vue.set(this, name, res.data)
                this.$emit('GET_AJAX_COMPLETE')
            })
        },
    },

    created: function() {
        this.search()
    },

    mounted: function() {
    },

    updated: function() {

    }
})