export const serverUrl = 'http://127.0.0.1:8000';

export function myFetch (url, opts) {
    return fetch(serverUrl + url, opts)
}