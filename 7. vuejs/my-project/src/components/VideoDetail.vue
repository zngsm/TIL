<template>
  <div v-if="video">
    비디오 디테일
    <iframe :src="videoSrc" frameborder="100"></iframe>
    <h2>{{ title }}</h2>
    <p>{{ description }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  props: {
    video: [Object, String]
  },
  computed: {
    videoSrc() {
      return `https://youtube.com/embed/${this.video.id.videoId}`
    },
    title() {
      return _.unescape(this.video.snippet.title)
    },
    description() {
      return _.unescape(this.video.snippet.description)
    }
  }
}
</script>

<style scoped>
  div {
    color:red;
    background-color: brown;
  }
</style>