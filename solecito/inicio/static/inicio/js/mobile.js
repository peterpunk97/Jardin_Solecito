<script>
    document.addEventListener('DOMContentLoaded', function () {
        var menuToggle = document.getElementById('menu-toggle');
        var mobileMenu = document.querySelector('.mobile-menu ul');

        menuToggle.addEventListener('click', function () {
            mobileMenu.classList.toggle('active');
        });
    });
</script>
