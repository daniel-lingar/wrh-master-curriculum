// WRH Master Curriculum - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
  initMobileMenu();
  initSmoothScroll();
  initProgressTracking();
});

/**
 * Initialize mobile menu toggle
 */
function initMobileMenu() {
  const menuToggle = document.querySelector('.menu-toggle');
  const navMenu = document.querySelector('nav ul');

  if (menuToggle && navMenu) {
    menuToggle.addEventListener('click', function() {
      navMenu.classList.toggle('active');
    });

    // Close menu when a link is clicked
    const navLinks = navMenu.querySelectorAll('a');
    navLinks.forEach(link => {
      link.addEventListener('click', function() {
        navMenu.classList.remove('active');
      });
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
      if (!event.target.closest('header')) {
        navMenu.classList.remove('active');
      }
    });
  }
}

/**
 * Smooth scroll behavior for anchor links
 */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  });
}

/**
 * Track reading progress and update UI
 */
function initProgressTracking() {
  const progressBar = document.querySelector('.progress-bar');
  if (!progressBar) return;

  window.addEventListener('scroll', function() {
    const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (window.scrollY / windowHeight) * 100;
    progressBar.style.width = scrolled + '%';
  });
}

/**
 * Utility: Add active class to current nav link
 */
function setActiveNavLink() {
  const currentLocation = location.pathname;
  const menuItems = document.querySelectorAll('nav a');

  menuItems.forEach(item => {
    if (item.getAttribute('href') === currentLocation) {
      item.classList.add('active');
    }
  });
}

/**
 * Utility: Format date
 */
function formatDate(date) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(date).toLocaleDateString('en-US', options);
}

/**
 * Utility: Show/hide elements with fade effect
 */
function fadeToggle(element, duration = 300) {
  if (element.style.display === 'none' || !element.style.display) {
    fadeIn(element, duration);
  } else {
    fadeOut(element, duration);
  }
}

function fadeIn(element, duration = 300) {
  element.style.display = 'block';
  element.style.opacity = '0';
  let opacity = 0;
  const step = 1 / (duration / 10);

  const interval = setInterval(() => {
    opacity += step;
    element.style.opacity = opacity;
    if (opacity >= 1) {
      clearInterval(interval);
      element.style.opacity = '1';
    }
  }, 10);
}

function fadeOut(element, duration = 300) {
  let opacity = 1;
  const step = 1 / (duration / 10);

  const interval = setInterval(() => {
    opacity -= step;
    element.style.opacity = opacity;
    if (opacity <= 0) {
      clearInterval(interval);
      element.style.display = 'none';
    }
  }, 10);
}

/**
 * Modal functionality
 */
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
  }
}

// Close modal when clicking outside
document.addEventListener('click', function(event) {
  if (event.target.classList.contains('modal')) {
    event.target.classList.remove('active');
    document.body.style.overflow = 'auto';
  }
});

/**
 * Form validation
 */
function validateForm(formId) {
  const form = document.getElementById(formId);
  if (!form) return false;

  const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
  let isValid = true;

  inputs.forEach(input => {
    if (!input.value.trim()) {
      input.classList.add('error');
      isValid = false;
    } else {
      input.classList.remove('error');
    }
  });

  return isValid;
}

/**
 * Export functions for global use
 */
window.WRH = {
  openModal,
  closeModal,
  fadeToggle,
  fadeIn,
  fadeOut,
  validateForm,
  formatDate,
  setActiveNavLink
};
