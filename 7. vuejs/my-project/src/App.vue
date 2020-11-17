<template>
  <div>
    <SearchBar 
    :userInput="userInput"
    @changeUserInput="onChangeUserInput"
    />
    <VideoList :videos="videos" @select_video="onVideoSelect"/>
    <VideoDetail :video="selectedVideo"/>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
import VideoDetail from './components/VideoDetail'

export default {
  name: 'App',
  components : {
    SearchBar,
    VideoList,
    VideoDetail
  },
  data() {
    return {
      userInput: '',
      videos: [],
      selectedVideo: '',
    }
  },
  methods: {
    onChangeUserInput(input) {
      this.userInput = input
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      const API_KEY = 'AIzaSyCF0X00vPGkrhfEy8g8aNYI15Eq6256gG0'
      if (this.userInput === '') {
        return
      }
      axios({
        url: API_URL,
        method: 'GET',
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.userInput
        }
      }).then(res=>{
        this.videos = res.data.items
        console.log(res.data.items)
      }).catch(err=>{
        console.error(err)
      })
    },
    onVideoSelect (video) {
      this.selectedVideo = video
    }
  },
  watch: {
    userInput(value) {
      // console.log('watch', value) // 해당 data를 감시해서 변경되면, 실행!
      if (value === 'bad') {
        alert('말조심!')
        this.userInput = ''
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<!--
App / data : userInput, videos ( videos는 videolist와 videodetail에서 쓸 수 있음 -> 둘은 형제 관계이기 때문에 부모인 app에다가 만들면 됨, userinput와 video는 종속관계이기 때문에 같은 곳에서 넣어줘야한다)
-->