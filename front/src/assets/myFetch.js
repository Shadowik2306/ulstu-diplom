export const serverUrl = '/api';

export function myFetch (url, opts) {
    if (opts === undefined) {
        opts = {};
    }
    if (opts.headers === undefined) {
        opts.headers = {}
    }
    const token = JSON.parse(localStorage.getItem('vrs_')).token;
    if (token) {
        opts.headers.Authorization = "Bearer " + token;
    }
    return fetch(
        serverUrl + url,
        opts
    )
}

