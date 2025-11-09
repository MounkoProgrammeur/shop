
const toggle = document.getElementById('menu-toggle');
  const nav = document.getElementById('nav');

  toggle.addEventListener('click', () => {
    nav.classList.toggle('active');
    toggle.classList.toggle('active');
  });



let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;
const sliderWrapper = document.getElementById('sliderWrapper');
const dotsContainer = document.getElementById('sliderDots');


for (let i = 0; i < totalSlides; i++) {
    const dot = document.createElement('div');
    dot.className = 'dot';
    if (i === 0) dot.classList.add('active');
    dot.onclick = () => goToSlide(i);
    dotsContainer.appendChild(dot);
}

const dots = document.querySelectorAll('.dot');

function updateSlider() {
    sliderWrapper.style.transform = `translateX(-${currentSlide * 100}%)`;
    
    // Mettre à jour les dots
    dots.forEach((dot, index) => {
        if (index === currentSlide) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

function changeSlide(direction) {
    currentSlide += direction;
    
    if (currentSlide < 0) {
        currentSlide = totalSlides - 1;
    } else if (currentSlide >= totalSlides) {
        currentSlide = 0;
    }
    
    updateSlider();
}

function goToSlide(index) {
    currentSlide = index;
    updateSlider();
}

// Défilement automatique toutes les 4 secondes
setInterval(() => {
    changeSlide(1);
}, 4000);