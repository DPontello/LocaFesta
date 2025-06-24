// funções de requisição à API

const API_BASE_URL = 'http://localhost:5000/api';

async function apiRequest(endpoint, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
        }
    };
    if (data) options.body = JSON.stringify(data);

    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
        const result = await response.json();
        if (!response.ok) throw new Error(result.error || 'Erro na requisição');
        return result;
    } catch (error) {
        console.error('Erro na API:', error);
        throw error;
    }
}