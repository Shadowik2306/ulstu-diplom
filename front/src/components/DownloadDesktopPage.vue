<template>
  <div class="file-downloads">
    <h1>Download Files</h1>
    <ul>
      <li v-for="file in files" :key="file.id">
        <span>{{ file.name }}</span>
        <button @click="downloadFile(file.file_name)">Download</button>
      </li>
    </ul>
  </div>
</template>

<script>
import {myFetch, serverUrl} from "../assets/myFetch.js";

export default {
  data() {
    return {
      files: [
        { id: 1, name: "Desktop file for MacOS on Intel", file_name: "Tinkling_Mac_Intel.zip" },
        { id: 2, name: "Desktop file for MacOS on ARM", file_name: "Tinkling_Mac_ARM.zip" },
        { id: 3, name: "Desktop file for Windows", file_name: "Tinkling_Windows.zip" }
      ]
    };
  },
  methods: {
    downloadFile(file_name) {
      window.location.replace(`${serverUrl}/files/${file_name}`)
    }
  }
};
</script>

<style>
.file-downloads {
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
  color: black;
}
.file-downloads h1 {
  margin-bottom: 20px;
}
.file-downloads ul {
  list-style: none;
  padding: 0;
}
.file-downloads li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.file-downloads button {
  padding: 5px 10px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.file-downloads button:hover {
  background-color: #0056b3;
}
</style>