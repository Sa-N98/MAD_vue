
const app = Vue.createApp({

                          data(){

                                return {
                                        searchTag:'',
                                        searchQuery:'',
                                        songs:''
                                        }
                                },

                          mounted(){
                                    //    app logic
                                    },
                          methods: {

                                    query: function(event) { 
                                                            event.preventDefault()
                                                            console.log(this.searchTag)
                                                            console.log(this.searchQuery)

                                                            fetch('/api/songs/' + this.searchTag + '/'+ this.searchQuery)
                                                            .then(response => response.json())
                                                            .then(data => {
                                                                                 console.log(data['api_data'])
                                                                                 this.songs= data['api_data']
                                                                            }
                                                            )
                                                                
                                                               
                                                        },
                                   
                                    }
                            })
                         
app.mount('#app')