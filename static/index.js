<script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>


    $('.navbar-toggler').click(function() {
      $(this).toggleClass('active');
      $('.navigation-menu').toggleClass('hidden');
      $('#navbar').addClass('bg-white');
    });
    $(function() {
      var navigation = $("#navbar");
      $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll >= 10) {
          navigation.addClass("bg-white xl:py-4 shadow-md");
          navigation.removeClass("xl:py-8");
        } else {
          navigation.removeClass("bg-white xl:py-4 shadow-md");
          navigation.addClass("xl:py-8");
        }
      });
    });

    window.onload = function() {
      const urlParams = new URLSearchParams(window.location.search);
      const uploadedImageUrl = urlParams.get('image');
      if (uploadedImageUrl) {
          document.getElementById('uploadedImage').src = uploadedImageUrl;
      }
  };

  document.getElementById('profileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function(e) {
      document.getElementById('profileImage').src = e.target.result;
    };
    reader.readAsDataURL(file);
  });