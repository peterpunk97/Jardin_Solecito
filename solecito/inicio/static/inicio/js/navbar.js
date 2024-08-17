<script>
    document.addEventListener('DOMContentLoaded', function() {
        var menuToggle = document.getElementById('menu-toggle');
    var mobileMenu = document.querySelector('.mobile-menu');

    // Función para alternar el menú móvil
    menuToggle.addEventListener('click', function() {
            if (mobileMenu.style.display === 'block') {
        mobileMenu.style.display = 'none';
            } else {
        mobileMenu.style.display = 'block';
            }
        });
    });
</script>
