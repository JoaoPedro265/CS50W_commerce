<img style="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&section=header&fontColor=FFFFFF&theme=cobalt" />

<h1 align="left">⚖️ Commerce - Plataforma de Leilões (CS50W)</h1>

<p align="left">
Uma aplicação robusta de e-commerce baseada em leilões, desenvolvida com <strong>Django</strong>. Este projeto foca na lógica de backend para gerenciar transações em tempo real, estados de anúncios e interações entre usuários autenticados.
</p>

###

<h2 align="left">🚀 Funcionalidades Principais</h2>

<ul>
<li><strong>Leilões Ativos:</strong> Visualização de todos os itens disponíveis com fotos e descrições.</li>
<li><strong>Criação de Listings:</strong> Usuários autenticados podem cadastrar novos itens (Título, Descrição, Lance Inicial, Categoria e Imagem).</li>
<li><strong>Sistema de Lances:</strong> Validação lógica onde o novo lance deve ser maior que o atual.</li>
<li><strong>Watchlist (Lista de Desejos):</strong> Adicione ou remova itens do seu interesse para acompanhar de perto.</li>
<li><strong>Categorias:</strong> Filtro inteligente de produtos por nicho (Eletrônicos, Moda, Brinquedos, etc.).</li>
<li><strong>Comentários:</strong> Espaço para interação e dúvidas em cada anúncio.</li>
<li><strong>Encerramento de Leilão:</strong> O criador do anúncio pode encerrá-lo, declarando o maior licitante como vencedor.</li>
<li><strong>Painel Admin:</strong> Gerenciamento total via Django Admin.</li>
</ul>

<h2 align="left">🧠 Modelagem de Dados (Banco de Dados)</h2>

<p align="left">
O coração deste projeto é a relação entre modelos no SQLite/PostgreSQL:
</p>

<ul>
<li><strong>User:</strong> Autenticação e perfil do usuário.</li>
<li><strong>Auction Listings:</strong> Detalhes do produto e status (Ativo/Encerrado).</li>
<li><strong>Bids:</strong> Histórico de lances vinculados a usuários e produtos.</li>
<li><strong>Comments:</strong> Feedback e interações.</li>
</ul>

<h2 align="left">🛠️ Tecnologias Utilizadas</h2>

<div align="left">
<img src="https://skillicons.dev/icons?i=py,django,html,css,sqlite" height="40" />
</div>
<h2 align="left">📺 Demonstração em Vídeo</h2>

<div align="center">

https://github.com/user-attachments/assets/3b7d4622-4170-4a03-99fc-895eb0e018f0

  <br />
  <p>
    <a href="https://youtu.be/Z-McM0AQdw0" target="_blank">
      <strong>🚀 <i>Confira a demonstração no YouTube:</i></strong>
    </a>
  </p>
</div>

---
