console.log("The script is running!");

const body = document.querySelector('body');

for (i = 0; i < 10; i++) {
    const dummy_element = document.createElement('p');
    dummy_element.innerText = `Can you believe this is working? [${i}]`;

    setTimeout(() => {
        body.appendChild(dummy_element);
    }, i * 1000)
}

console.log("The script finished!")