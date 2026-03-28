/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*.html',
    './**/*.html',
    './assets/js/**/*.js',
    './components/**/*.html',
    './scripts/**/*.py',
    './*.py',
  ],
  theme: {
    extend: {
      colors: {
        gold: '#C39847',
        noir: '#0D0D0D',
      },
      fontFamily: {
        montserrat: ['Montserrat', 'sans-serif'],
      },
      boxShadow: {
        'gold/20': '0 0 24px rgba(195, 152, 71, 0.2)',
        'gold/30': '0 0 40px rgba(195, 152, 71, 0.3)',
        'gold/40': '0 0 40px rgba(195, 152, 71, 0.4)',
      },
    },
  },
  plugins: [],
};
