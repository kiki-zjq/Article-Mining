# Web Template

It is a project based on Vue.js

After `npm run dev` it will default load at localhost:8081

If you haven't configured NPM yet, you can still view the final result directly by `./docs/index.html`

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8081 or 8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

## How to modify the code 

1. If you want to add a totally new page 
    => Go to `src/layout/header.vue` add a new entrance.
    => Go to `src/view` add a new folder and add a file named `index.vue` in this folder.
    => Go to `src/router/index.js` add new router information. 

2. If you want to change something on the page (For exampe,I want to modify 'homepage')
    => Go to `src/view/homepage/index.vue` 

## Important

After you finishing all your modify.Just use `npm run build`,and new version of webpage have been compiled.
You can see the result in folder named `doc`.
After you using `npm run build`,please delete unnecessary <link> and <script> tag in `./doc/index.html`