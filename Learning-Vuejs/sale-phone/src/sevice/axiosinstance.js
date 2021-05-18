const { default: Axios } = require('axios');

const axiosinstance = Axios.create({
    baseURL: 'http://laravel-react-sell-web.herokuapp.com/',
});

// axiosinstance.defaults.headers.common['leelainstance'] =
//     'leela instance header';

export default axiosinstance;