<template>
  <div>
    <input type="text" 
    :value="userInput"
    @change="onChange"
    >
  </div>
</template>

<script>
export default {
  props: {
    userInput: {
      type: String,
      //{userInput: String} 으로 해줘도 무방하다!
      required: true, // 안넘겨주면 안된다!!를 명시해주는 것
    }
  },
  methods: {
    onChange(event) {
      this.$emit('changeUserInput', event.target.value)
    }
  }

}
</script>

<style>

</style>