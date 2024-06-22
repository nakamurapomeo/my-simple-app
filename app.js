document.getElementById('novelForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const keywords = document.getElementById('keywords').value;
    const genres = [];
    if (document.getElementById('fantasy').checked) genres.push('fantasy');
    if (document.getElementById('romance').checked) genres.push('romance');

    const response = await fetch('/generate-novel', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ keywords, genres })
    });

    const result = await response.json();
    document.getElementById('result').innerText = result.novel;
});
