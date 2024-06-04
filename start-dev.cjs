const { exec } = require('child_process');
const waitOn = require('wait-on');

// Caminho completo para o arquivo App.py
const flaskScript = 'python C:\\Users\\rhadu\\Desktop\\jogo-da-velha-master\\src\\App.py';

// Iniciar o servidor Flask
const flaskProcess = exec(flaskScript);

flaskProcess.stdout.on('data', (data) => {
  console.log(`Flask: ${data}`);
});

flaskProcess.stderr.on('data', (data) => {
  console.error(`Flask Error: ${data}`);
});

// Aguardar o servidor Flask estar disponível
waitOn({ resources: ['http://localhost:5000'] }, (err) => {
  if (err) {
    console.error('Erro ao aguardar o servidor Flask:', err);
    process.exit(1);
  }

  // Iniciar o front-end React
  const reactProcess = exec('npm run start-react');

  reactProcess.stdout.on('data', (data) => {
    console.log(`React: ${data}`);
  });

  reactProcess.stderr.on('data', (data) => {
    console.error(`React Error: ${data}`);
  });
});
