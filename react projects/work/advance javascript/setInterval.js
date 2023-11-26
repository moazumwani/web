let timerId =setInterval(() =>  alert('tick'), 2000);
setTimeout(() => { clearInterval(timerId); alert ('stop');
    
}, 5000);