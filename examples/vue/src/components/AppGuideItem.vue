<script>
export default {
  props: {
    href: String,
    text: String
  }
}
</script>

<template>
  <li class="d-flex align-items-center mb-2">
    <a :href="href" target="_blank" rel="noopener">{{ text }}</a>
  </li>
</template>
