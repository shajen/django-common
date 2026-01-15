function setTheme(theme) {
    localStorage.setItem('theme', theme);
    document.documentElement.setAttribute('data-bs-theme', theme);
}

function updateTheme() {
    const storedTheme = localStorage.getItem('theme');
    const preferredTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    document.documentElement.setAttribute('data-bs-theme', storedTheme || preferredTheme);
}
