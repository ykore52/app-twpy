$(function () {
    var browserLanguage = (window.navigator.languages && window.navigator.languages[0]) ||
        window.navigator.language ||
        window.navigator.userLanguage ||
        window.navigator.browserLanguage

    let app = new Vue({
        el: '#tweetApp',
        data: {
            searchWord: "",
            fetchedTweets: {}
        },
        methods: {
            submitSearch: function () {

                if (rv = this.searchWord.match(/[@]([a-zA-Z0-9_]+)/)) {
                    this.getUserTimeline(rv[1])
                } else {
                    if (this.searchWord == "") return

                    let searchParams = {
                        'q': this.searchWord,
                        'result_type': 'recent',
                        'count': 10,
                    }

                    let params = new URLSearchParams(searchParams)
                    this.search(params)
                }
            },

            getUserTimeline: function (screen_name) {
                return axios.get("/api/statuses/user_timeline/" + screen_name)
                    .then(this._addFormattedDateTime)
            },

            search: function (url) {
                return axios.get("/api/search?" + url)
                    .then(this._addFormattedDateTime)
            },

            _addFormattedDateTime: function (res) {
                this.fetchedTweets = JSON.parse(res.data)
                var options = {
                    weekday: "long",
                    year: "numeric",
                    month: "short",
                    day: "numeric",
                    hour: "2-digit",
                    minute: "2-digit",
                    second: "2-digit"
                }
                for (let i = 0; i < this.fetchedTweets.tweets.length; i++) {
                    let tweet = this.fetchedTweets.tweets[i]
                    this.fetchedTweets.tweets[i].formatted_datetime = new Date(this.fetchedTweets.tweets[i].created_at).toLocaleDateString(browserLanguage, options)
                }
                this.$emit('GET_AJAX_COMPLETE')
            },

            expand: function (tweet) {
                collapsed_urls = tweet.text.match(/(http|https):\/\/[^ ]+/g)
                last_collapsed_url = collapsed_urls.pop()
                urls = tweet.urls
                console.log(JSON.stringify(urls))
                filtered = urls.filter(e => {
                    console.log(e.url + ":" + last_collapsed_url)
                    return e.url === last_collapsed_url
                })
            },

            expandRetweet: function (id) {
                return axios.get("/api/status/" + id)
                    .then((res) => {
                        $("." + id).val(res.data)
                    })
            },
        },

        created: function () {
            this.search()
        },

        mounted: function () {},

        updated: function () {

        }
    })
})