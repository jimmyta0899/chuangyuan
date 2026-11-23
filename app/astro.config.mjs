import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.chuangyuancorp.com',
  trailingSlash: 'always',
  integrations: [
    sitemap({
      filter: (page) => page !== 'https://www.chuangyuancorp.com/',
      i18n: {
        defaultLocale: 'en',
        locales: { en: 'en-US', zh: 'zh-CN' },
      },
    }),
  ],
  build: {
    output: 'static',
  },
});
