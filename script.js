const navToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });
}

document.querySelectorAll('.nav-links a').forEach((link) => {
  if (window.location.pathname.endsWith(link.getAttribute('href'))) {
    link.classList.add('active');
  }
});

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.16 });

document.querySelectorAll('.reveal').forEach((item) => revealObserver.observe(item));

const animateCounter = (element) => {
  const target = Number(element.dataset.target || 0);
  const suffix = element.dataset.suffix || '';
  const duration = 1400;
  const startTime = performance.now();

  const step = (currentTime) => {
    const progress = Math.min((currentTime - startTime) / duration, 1);
    const value = Math.floor(progress * target);
    element.textContent = `${value}${suffix}`;
    if (progress < 1) {
      requestAnimationFrame(step);
    } else {
      element.textContent = `${target}${suffix}`;
    }
  };

  requestAnimationFrame(step);
};

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting && !entry.target.dataset.animated) {
      entry.target.dataset.animated = 'true';
      animateCounter(entry.target);
    }
  });
}, { threshold: 0.8 });

document.querySelectorAll('.stat strong').forEach((counter) => counterObserver.observe(counter));

document.getElementById('year').textContent = new Date().getFullYear();

const forms = document.querySelectorAll('form');
forms.forEach((form) => {
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const note = form.querySelector('.success');
    if (note) {
      note.style.display = 'block';
      note.textContent = 'Thank you! We will connect with you shortly.';
    }
    form.reset();
  });
});
