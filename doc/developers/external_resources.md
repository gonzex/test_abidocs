---
rpath: developers/external_resources.md
light_gallery: true
---

<div id="video-gallery" class="gallery">
  <a href="https://www.youtube.com/watch?v=DppLQ-KQA68">
    <img src="//img.youtube.com/vi/DppLQ-KQA68/default.jpg">
  </a>
  <a href="https://youtu.be/EfJcYi1MNBg">
    <img src="//img.youtube.com/vi/EfJcYi1MNBg/default.jpg">
  </a>
  <a href="https://www.youtube.com/watch?v=gcbfb_Mteo4">
    <img src="//img.youtube.com/vi/gcbfb_Mteo4/default.jpg">
  </a>
  <a href="https://youtu.be/UNlRHw9Avvw">
    <img src="//img.youtube.com/vi/UNlRHw9Avvw/default.jpg">
  </a>
  <a href="https://youtu.be/j9z4AJIx40M">
    <img src="//img.youtube.com/vi/j9z4AJIx40M/default.jpg">
  </a>
</div>

<script>
$(function() {
    // Automatic video thumbnails
    //$('#video-gallery').lightGallery();
    $('#video-gallery').lightGallery({
        loadYoutubeThumbnail: true,
        youtubeThumbSize: 'default',
        loadVimeoThumbnail: true,
        vimeoThumbSize: 'thumbnail_medium'
    }); 
});
</script>
