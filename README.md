# shield_land.js
Web-API for [shield.land](https://shield.land) project that was created by russian minecraft youtubers

## Example
```JavaScript
async function main() {
	const { ShieldLand } = require("./shield_land.js")
	const shieldLand = new ShieldLand()
	await shieldLand.login("email", "password")
}

main()
```
