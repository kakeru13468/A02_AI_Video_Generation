const express = require('express');
const {spawn} = require('child_process');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static(__dirname));
const absolutePath = path.join(__dirname, '../')

app.post('/generate', (req, res) => {
	if (res);

	var prompt = req.query.prompt;
	if (req.query.dry_run) var dry_run = true;


	let args = [path.join(absolutePath, 'main.py'), prompt, dry_run? '--dry-run' : ''];

	let child_process = spawn('python', args);
	
	child_process.stdout.on('data', (data) => {
		console.log(`stdout: ${data}`);
	});
	child_process.stderr.on('data', (data) => {
		console.log(`stderr: ${data}`);
	});
});

app.listen(port, () => console.log(`App listening on port ${port}.`))