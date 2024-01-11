#!/usr/bin/node
const dict = require('./101-data').dict;

const invertedDict = {};

for (const userId in dict) {
	const occurences = dict[userId];

	if (!invertedDict[occurences]) {
		invertedDict[occurences] = [];
	}

	invertedDict[occurences}.push(userId);
}

console.log(invertedDict);
