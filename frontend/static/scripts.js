async function setMiddleware(middleware) {
    let resp = await fetch('http://localhost:5000/set_middleware', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({middleware})
    });
    let data = await resp.json();
    alert(data.status || data.error);
    getMiddleware();
}

async function getMiddleware() {
    let resp = await fetch('http://localhost:5000/get_middleware');
    let data = await resp.json();
    document.getElementById('middleware_status').innerText = "Middleware atual: " + data.middleware;
}

document.addEventListener('DOMContentLoaded', function() {
    getMiddleware();
    let select = document.getElementById('middleware_select');
    if (select) {
        select.onchange = function() {
            setMiddleware(this.value);
        };
    }

    let form = document.getElementById('solicitacao');
    if (form) {
        form.onsubmit = async function(e) {
            e.preventDefault();
            let cliente = document.getElementById('cliente').value;
            let descricao = document.getElementById('descricao').value;
            let resp = await fetch('http://localhost:5000/solicitar_manutencao', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({cliente, descricao})
            });
            let data = await resp.json();
            document.getElementById('resposta').innerText = data.status;
        };
    }

    let aprovacao = document.getElementById('aprovacao');
    if (aprovacao) {
        aprovacao.onsubmit = async function(e) {
            e.preventDefault();
            let ordem_id = document.getElementById('ordem_id').value;
            let aprovado = document.getElementById('aprovado').value;
            let resp = await fetch('http://localhost:5000/aprovar_orcamento', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ordem_id, aprovado})
            });
            let data = await resp.json();
            document.getElementById('resposta').innerText = data.status;
        };
    }
});

async function listarOrdens() {
    let resp = await fetch('http://localhost:5001/listar_ordens');
    let data = await resp.json();
    let ul = document.getElementById('ordens');
    ul.innerHTML = '';
    for (let id in data) {
        let li = document.createElement('li');
        li.innerText = `ID: ${id} | Cliente: ${data[id].cliente} | Status: ${data[id].status}`;
        ul.appendChild(li);
    }
}
