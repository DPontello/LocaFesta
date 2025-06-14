// URL base da API
const API_BASE_URL = 'http://localhost:5000/api';

let editingClienteId = null;

// Função para fazer requisições à API
async function apiRequest(endpoint, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
        }
    };
    
    if (data) {
        options.body = JSON.stringify(data);
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
        const result = await response.json();
        
        if (!response.ok) {
            throw new Error(result.error || 'Erro na requisição');
        }
        
        return result;
    } catch (error) {
        console.error('Erro na API:', error);
        throw error;
    }
}

// Carregar e exibir clientes na tabela
async function loadClientes() {
    try {
        const clientes = await apiRequest('/clientes');
        const tableBody = document.getElementById('clientesTableBody');
        
        tableBody.innerHTML = '';
        
        clientes.forEach(cliente => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${cliente.idCliente}</td>
                <td>${cliente.nomeCliente}</td>
                <td>${cliente.cpfCnpjCliente}</td>
                <td>${cliente.emailCliente}</td>
                <td>${cliente.telefoneCliente}</td>
                <td>
                    <button class="btn btn-sm btn-primary" onclick="editCliente(${cliente.idCliente})">
                        Editar
                    </button>
                    <button class="btn btn-sm btn-danger" onclick="deleteCliente(${cliente.idCliente})">
                        Deletar
                    </button>
                </td>
            `;
            tableBody.appendChild(row);
        });
        
    } catch (error) {
        console.error('Erro ao carregar clientes:', error);
        alert('Erro ao carregar clientes: ' + error.message);
    }
}

// Abrir modal para adicionar novo cliente
function showAddClienteModal() {
    editingClienteId = null;
    document.getElementById('clienteModalTitle').textContent = 'Adicionar Cliente';
    document.getElementById('clienteForm').reset();
    const modal = new bootstrap.Modal(document.getElementById('clienteModal'));
    modal.show();
}

// Editar cliente
async function editCliente(id) {
    try {
        editingClienteId = id;
        const cliente = await apiRequest(`/clientes/${id}`);
        
        document.getElementById('clienteModalTitle').textContent = 'Editar Cliente';
        document.getElementById('nomeCliente').value = cliente.nomeCliente;
        document.getElementById('cpfCnpjCliente').value = cliente.cpfCnpjCliente;
        document.getElementById('emailCliente').value = cliente.emailCliente;
        document.getElementById('telefoneCliente').value = cliente.telefoneCliente;
        
        const modal = new bootstrap.Modal(document.getElementById('clienteModal'));
        modal.show();
        
    } catch (error) {
        console.error('Erro ao carregar cliente:', error);
        alert('Erro ao carregar cliente: ' + error.message);
    }
}

// Salvar cliente (adicionar ou editar)
async function saveCliente() {
    const nome = document.getElementById('nomeCliente').value.trim();
    const cpfCnpj = document.getElementById('cpfCnpjCliente').value.trim();
    const email = document.getElementById('emailCliente').value.trim();
    const telefone = document.getElementById('telefoneCliente').value.trim();
    
    if (!nome || !cpfCnpj || !email || !telefone) {
        alert('Por favor, preencha todos os campos.');
        return;
    }

    if (!validatePhone(telefone)) {
        alert('Telefone inválido. Deve conter 10 ou 11 dígitos.');
        return;
    }

    if (!validateEmail(email)) {
    alert('E-mail inválido. Verifique o formato.');
    return;
}
    
    const clienteData = {
        nomeCliente: nome,
        cpfCnpjCliente: cpfCnpj,
        emailCliente: email,
        telefoneCliente: telefone
    };
    
    try {
        if (editingClienteId) {
            // Editar cliente existente
            await apiRequest(`/clientes/${editingClienteId}`, 'PUT', clienteData);
            alert('Cliente atualizado com sucesso!');
        } else {
            // Adicionar novo cliente
            await apiRequest('/clientes', 'POST', clienteData);
            alert('Cliente adicionado com sucesso!');
        }
        
        // Fechar modal e recarregar tabela
        bootstrap.Modal.getInstance(document.getElementById('clienteModal')).hide();
        await loadClientes();
        
    } catch (error) {
        console.error('Erro ao salvar cliente:', error);
        alert('Erro ao salvar cliente: ' + error.message);
    }
}

// Deletar cliente
async function deleteCliente(id) {
    if (confirm('Tem certeza que deseja excluir este cliente?')) {
        try {
            await apiRequest(`/clientes/${id}`, 'DELETE');
            alert('Cliente excluído com sucesso!');
            await loadClientes();
        } catch (error) {
            console.error('Erro ao excluir cliente:', error);
            alert('Erro ao excluir cliente: ' + error.message);
        }
    }
}

// Formatação de telefone
function formatPhone(value) {
    const numbers = value.replace(/\D/g, '');
    if (numbers.length === 11) {
        return numbers.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
    } else if (numbers.length === 10) {
        return numbers.replace(/(\d{2})(\d{4})(\d{4})/, '($1) $2-$3');
    }
    return value;
}

// Validação básica de CPF/CNPJ
function validateCpfCnpj(value) {
    const numbers = value.replace(/\D/g, '');
    return numbers.length === 11 || numbers.length === 14;
}

// Validação de telefone (10 ou 11 dígitos)
function validatePhone(value) {
    const numbers = value.replace(/\D/g, '');
    return numbers.length === 10 || numbers.length === 11;
}

// Validação de e-mail com regex simples
function validateEmail(value) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(value);
}


// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    // Carregar clientes ao carregar a página
    loadClientes();
    
    // Formatação automática do telefone
    const telefoneInput = document.getElementById('telefoneCliente');
    if (telefoneInput) {
        telefoneInput.addEventListener('input', function(e) {
            e.target.value = formatPhone(e.target.value);
        });
    }

    // Validação do telefone
    if (telefoneInput) {
        telefoneInput.addEventListener('blur', function(e) {
            if (e.target.value && !validatePhone(e.target.value)) {
                alert('Telefone inválido. Deve conter 10 ou 11 dígitos.');
            }
        });
    }

    // Validação do e-mail
    const emailInput = document.getElementById('emailCliente');
    if (emailInput) {
        emailInput.addEventListener('blur', function(e) {
            if (e.target.value && !validateEmail(e.target.value)) {
                alert('E-mail inválido. Verifique o formato.');
            }
        });
    }

    // Formatação automática do CPF/CNPJ
    const cpfCnpjInput = document.getElementById('cpfCnpjCliente');
    if (cpfCnpjInput) {
        cpfCnpjInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            
            if (value.length <= 11) {
                // Formato CPF
                value = value.replace(/(\d{3})(\d)/, '$1.$2');
                value = value.replace(/(\d{3})(\d)/, '$1.$2');
                value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
            } else {
                // Formato CNPJ
                value = value.replace(/^(\d{2})(\d)/, '$1.$2');
                value = value.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
                value = value.replace(/\.(\d{3})(\d)/, '.$1/$2');
                value = value.replace(/(\d{4})(\d)/, '$1-$2');
            }
            
            e.target.value = value;
        });
    }
    
    // Validação do CPF/CNPJ
    if (cpfCnpjInput) {
        cpfCnpjInput.addEventListener('blur', function(e) {
            if (e.target.value && !validateCpfCnpj(e.target.value)) {
                alert('CPF deve ter 11 dígitos ou CNPJ deve ter 14 dígitos');
            }
        });
    }
    
    // Submit do formulário
    const clienteForm = document.getElementById('clienteForm');
    if (clienteForm) {
        clienteForm.addEventListener('submit', function(e) {
            e.preventDefault();
            saveCliente();
        });
    }
});