#!/usr/bin/node
const args = process.argv;
if (!(parseInt(args[2]))) {
    console.log('Missing size');
} else {
    const x = args[2];
    let line = 'x';
    for (let i = 1; i < x; i++) {
        line += 'x';
    }
    for (let i = 0; i < x; i++) {
        console.log(line);
    }
}
