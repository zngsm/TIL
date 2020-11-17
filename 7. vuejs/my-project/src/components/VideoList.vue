<template>
  <div>
    <ul>
      <VideoListItem 
      v-for="video in videos" 
      :video="video" 
      :key="video.id.videoId"
      @select_video="onVideoSelect"
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem'

export default {
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    onVideoSelect (video) {
      this.$emit('select_video', video)
    }
  }
}
</script>

<style>

</style>