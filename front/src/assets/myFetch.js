export const serverUrl = 'http://127.0.0.1:8000';

export function myFetch (url, opts) {
    if (opts === undefined) {
        opts = {
            headers: {},
        };
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