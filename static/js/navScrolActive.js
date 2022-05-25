const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('nav div ul li')
window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset > (sectionTop - sectionHeight * .40)) {
            current = section.getAttribute('id');
        }
    })
    navLinks.forEach((navLink) => {
        navLink.classList.remove('active');
        if (navLink.classList.contains(current)) {
            navLink.classList.add('active');
            console.log(current)
        }
    })
})
