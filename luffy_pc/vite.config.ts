/*
 * @Author: sunjie
 * @Date: 2025-03-07 01:30:04
 * @LastEditors: sunj
 * @LastEditTime: 2025-03-08 18:59:40
 * @FilePath: /sunjPy/luffy_pc/vite.config.ts
 */
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server:{
    host:'www.sunj.com',
    port:3000
  }
})
