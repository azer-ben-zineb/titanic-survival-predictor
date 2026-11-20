/**
 * Titanic Survival Predictor - Client-side UI Enhancements
 */

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const submitBtn = document.getElementById('submit-btn');
    const spinner = document.getElementById('spinner');
    const loadingIndicator = document.getElementById('loading-indicator');
    const roleSelect = document.getElementById('id_Person_Role');
    const pclassSelect = document.getElementById('id_Pclass');

    // 1. Show spinner and disable button on form submission
    if (form && submitBtn) {
        form.addEventListener('submit', (e) => {
            // Check HTML5 validity before showing spinner
            if (form.checkValidity()) {
                submitBtn.disabled = true;
                if (spinner) spinner.classList.remove('hidden');
                if (loadingIndicator) loadingIndicator.classList.remove('hidden');
                submitBtn.style.opacity = '0.75';
            }
        });
    }

    // 2. Intelligent Pclass assistance based on Person_Role
    if (roleSelect && pclassSelect) {
        roleSelect.addEventListener('change', () => {
            const role = roleSelect.value;
            // Provide sensible defaults if Pclass is unselected
            if (role === 'Normal Passenger') {
                if (['Deck Crew', 'Engineering Crew', 'Victualling Crew', 'Restaurant Staff', 'Band'].includes(pclassSelect.value)) {
                    pclassSelect.value = '3';
                }
            } else if (role === 'Engineering Crew') {
                pclassSelect.value = 'Engineering Crew';
            } else if (role === 'Other Crew') {
                if (['1', '2', '3'].includes(pclassSelect.value) || !pclassSelect.value) {
                    pclassSelect.value = 'Victualling Crew';
                }
            }
        });
    }
});
