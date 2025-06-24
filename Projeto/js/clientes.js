// CRUD de clientes

let editingClienteId = null;

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
                    <button class="btn btn-sm btn-primary" onclick="editCliente(${cliente.idCliente})">Editar</button>
                    <button class="btn btn-sm btn-danger" onclick="deleteCliente(${cliente.idCliente})">Deletar</button>
                </td>`;
            tableBody.appendChild(row);
        });
    } catch (error) {
        alert('Erro ao carregar clientes: ' + error.message);
    }
}

function showAddClienteModal() {
    editingClienteId = null;
    document.getElementById('clienteModalTitle').textContent = 'Adicionar Cliente';
    document.getElementById('clienteForm').reset();
    new bootstrap.Modal(document.getElementById('clienteModal')).show();
}

async function editCliente(id) {
    try {
        editingClienteId = id;
        const cliente = await apiRequest(`/clientes/${id}`);
        document.getElementById('clienteModalTitle').textContent = 'Editar Cliente';
        document.getElementById('nomeCliente').value = cliente.nomeCliente;
        document.getElementById('cpfCnpjCliente').value = cliente.cpfCnpjCliente;
        document.getElementById('emailCliente').value = cliente.emailCliente;
        document.getElementById('telefoneCliente').value = cliente.telefoneCliente;
        new bootstrap.Modal(document.getElementById('clienteModal')).show();
    } catch (error) {
        alert('Erro ao carregar cliente: ' + error.message);
    }
}

async function saveCliente() {
    const nome = document.getElementById('nomeCliente').value.trim();
    const cpfCnpj = document.getElementById('cpfCnpjCliente').value.trim();
    const email = document.getElementById('emailCliente').value.trim();
    const telefone = document.getElementById('telefoneCliente').value.trim();

    const clienteData = { 
        nomeCliente: nome, 
        cpfCnpjCliente: cpfCnpj, 
        emailCliente: email, 
        telefoneCliente: telefone 
    };

    try {
        if (editingClienteId) {
            await apiRequest(`/clientes/${editingClienteId}`, 'PUT', clienteData);
            alert('Cliente atualizado com sucesso!');
        } else {
            await apiRequest('/clientes', 'POST', clienteData);
            alert('Cliente adicionado com sucesso!');
        }
        bootstrap.Modal.getInstance(document.getElementById('clienteModal')).hide();
        await loadClientes();
    } catch (error) {
        alert('Erro ao salvar cliente: ' + error.message);
    }
}

async function deleteCliente(id) {
    if (confirm('Deseja excluir este cliente?')) {
        try {
            await apiRequest(`/clientes/${id}`, 'DELETE');
            alert('Cliente excluído com sucesso!');
            await loadClientes();
        } catch (error) {
            alert('Erro ao excluir cliente: ' + error.message);
        }
    }
}