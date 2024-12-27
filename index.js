const puppeteer = require('puppeteer');
const { exec } = require('child_process');



(async () => {
    try {
    // free proxy server URL
        const proxyURL = 'socks4://localhost:9050';

        // launch a browser instance with the
        // --proxy-server flag enabled
        const browser = await puppeteer.launch({
            args: [`--proxy-server=${proxyURL}`],
        });
        const page = await browser.newPage();

        // Navega a la URL
        const url = 'https://httpbin.org/ip';
        await page.goto(url, { waitUntil: 'networkidle2' });
        let ip = await page.evaluate(() => {
            return document.body.innerText;
        })

        // Espera 5 segundos para asegurarte de que todo está cargado
        //await new Promise(resolve => setTimeout(resolve, 5000));

        // Toma una captura de pantalla
        await page.screenshot({ path: 'ip.png', fullPage: true });

        console.log(`Captura de pantalla guardada como pajar ${ip}.png`);

        // Cierra el navegador
        await browser.close();
        // Comando para ejecutar el script Python
        exec('python3 read.py', (error, stdout, stderr) => {
          if (error) {
              console.error(`exec error: ${error}`);
              return;
          }
          if (stderr) {
              console.error(`stderr: ${stderr}`);
              return;
          }
          console.log(`stdout: ${stdout}`);
        });
    } catch (error) {
        console.error('Hubo un error:', error);
    }
})();