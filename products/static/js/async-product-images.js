document.addEventListener('DOMContentLoaded', function () {
        var productImages = document.querySelectorAll('.product-image');

        productImages.forEach(function (image) {
                var src = image.getAttribute('data-src');
                if (src) {
                        image.setAttribute('src', src);
                }
        });
});
