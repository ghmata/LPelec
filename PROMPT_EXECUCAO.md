# 🔌 Prompt de Execução: Landing Page Premium - Eletricista Residencial

> **Objetivo:** Criar uma landing page de alta conversão, com design premium e minimalista, para um prestador de serviços elétricos residenciais em Rio Claro - SP.

---

## 📋 Briefing do Projeto

### Cliente
- **Negócio:** Eletricista Residencial
- **Localização:** Rio Claro, São Paulo
- **Área de Atendimento:** Toda a cidade de Rio Claro
- **Horário:** Segunda a Domingo, 08:00 às 20:00 (conforme disponibilidade)

### Objetivo da Landing Page
Gerar leads qualificados através do WhatsApp, transmitindo profissionalismo, confiança e urgência para serviços elétricos residenciais.

---

## 🎨 Sistema de Design (Design Tokens)

### Paleta de Cores

```css
/* Cores Primárias */
--primary-500: #2171ff;        /* Azul principal - CTAs, destaques */
--primary-600: #1a5cd4;        /* Azul hover */
--primary-700: #1347a8;        /* Azul pressed */

/* Cores de Conversão */
--whatsapp-500: #25D366;       /* Verde WhatsApp oficial */
--whatsapp-600: #1ebe5a;       /* Verde hover */
--whatsapp-glow: rgba(37, 211, 102, 0.3); /* Glow effect */

/* Cores Neutras */
--neutral-50: #f8fafc;         /* Background claro */
--neutral-100: #f1f5f9;        /* Cards, seções alternadas */
--neutral-200: #e2e8f0;        /* Bordas sutis */
--neutral-600: #475569;        /* Texto secundário */
--neutral-800: #1e293b;        /* Texto principal */
--neutral-900: #0f172a;        /* Títulos, footer */

/* Cores de Feedback */
--success: #10b981;            /* Disponível, confirmação */
--warning: #f59e0b;            /* Atenção, urgência */
```

### Tipografia

```css
/* Fonte Principal - Títulos */
font-family: 'Rubik', sans-serif;
/* Pesos: 500 (medium), 600 (semibold), 700 (bold) */

/* Fonte Secundária - Corpo */
font-family: 'Inter', sans-serif;
/* Pesos: 400 (regular), 500 (medium), 600 (semibold) */

/* Escala Tipográfica */
--text-xs: 0.75rem;      /* 12px */
--text-sm: 0.875rem;     /* 14px */
--text-base: 1rem;       /* 16px */
--text-lg: 1.125rem;     /* 18px */
--text-xl: 1.25rem;      /* 20px */
--text-2xl: 1.5rem;      /* 24px */
--text-3xl: 1.875rem;    /* 30px */
--text-4xl: 2.25rem;     /* 36px */
--text-5xl: 3rem;        /* 48px - Hero desktop */
```

### Espaçamento e Layout

```css
/* Container */
--container-max: 1200px;
--container-padding: 1.5rem;   /* 24px mobile */
--container-padding-lg: 4rem;  /* 64px desktop */

/* Seções */
--section-padding-y: 4rem;     /* 64px mobile */
--section-padding-y-lg: 6rem;  /* 96px desktop */

/* Bordas */
--radius-sm: 0.375rem;   /* 6px */
--radius-md: 0.5rem;     /* 8px */
--radius-lg: 0.75rem;    /* 12px */
--radius-xl: 1rem;       /* 16px */
--radius-full: 9999px;   /* Pílula */
```

### Sombras

```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
--shadow-glow-primary: 0 0 20px rgba(33, 113, 255, 0.3);
--shadow-glow-whatsapp: 0 0 20px rgba(37, 211, 102, 0.4);
```

---

## 📐 Estrutura de Seções

### 1. Header (Cabeçalho Fixo)

**Comportamento:**
- Fixo no topo (sticky)
- Background transparente → branco com blur ao scroll
- Altura: 72px desktop / 64px mobile
- Z-index elevado

**Elementos:**
```
[LOGO]                                    [Nav] [WhatsApp Button]
```

| Elemento | Especificação |
|----------|---------------|
| **Logo** | Imagem PNG/SVG à esquerda, altura máx 40px |
| **Navegação Desktop** | Links: "Início", "Serviços", "Sobre", "Contato" (âncoras suaves) |
| **Menu Mobile** | Ícone hambúrguer (☰) → Menu fullscreen overlay com animação slide-down |
| **Botão WhatsApp** | Pílula verde com ícone + "Orçamento" (desktop) / Apenas ícone (mobile) |

**Micro-interações:**
- Links: underline animado on hover
- Botão WhatsApp: pulse suave contínuo para chamar atenção

---

### 2. Hero Section (Seção Principal)

**Layout:** Centralizado, full-height (min 80vh mobile / 90vh desktop)

**Background:**
- Gradiente sutil: `linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%)`
- OU imagem abstrata de circuitos/eletricidade com overlay escuro (opacity 0.7)

**Conteúdo:**
```
[Badge de Disponibilidade]

TÍTULO PRINCIPAL (H1)

Subtítulo descritivo

[CTA Principal]    [CTA Secundário]

[Trust Badges / Social Proof]
```

| Elemento | Conteúdo | Estilo |
|----------|----------|--------|
| **Badge** | "⚡ Atendimento Rápido • Rio Claro - SP" | Pílula com borda, ícone animado |
| **H1** | "Soluções Elétricas Profissionais para Sua Residência" | 48px mobile / 64px desktop, bold, neutral-900 |
| **Subtítulo** | "Instalações, reparos e manutenções elétricas com segurança e garantia. Orçamento gratuito e atendimento ágil em toda Rio Claro." | 18px, neutral-600, max-width 600px |
| **CTA Principal** | "Agende seu Orçamento Grátis →" | Botão grande, verde WhatsApp, sombra glow |
| **CTA Secundário** | "Ver Nossos Serviços ↓" | Link estilo ghost/outline, azul primário |
| **Trust Badges** | "✓ +500 Clientes Atendidos" • "✓ 10 Anos de Experiência" • "⭐ 4.9 no Google" | Flex row, ícones sutis |

**Animações:**
- Elementos entram com fade-in + slide-up escalonado (stagger: 100ms)
- CTA principal com hover: scale(1.02) + shadow aumentada
- Seta do CTA com animação de bounce horizontal

---

### 3. Seção de Serviços

**Título da Seção:** "Nossos Serviços"
**Subtítulo:** "Soluções completas para todas as necessidades elétricas da sua casa"

**Layout:** Grid 2x2 (mobile) / 4 colunas (desktop)

**Cards de Serviço:**

| Serviço | Ícone | Descrição |
|---------|-------|-----------|
| Instalações Elétricas | 🔌 ou ícone Lucide `Plug` | Tomadas, interruptores, pontos de luz |
| Reparos e Manutenção | 🔧 ou `Wrench` | Conserto de curtos, quedas de energia |
| Quadros e Disjuntores | ⚡ ou `Zap` | Instalação e adequação de quadros elétricos |
| Iluminação | 💡 ou `Lightbulb` | Projetos de iluminação LED, spots, lustres |

**Estilo dos Cards:**
- Background branco
- Borda sutil (neutral-200)
- Ícone grande (48px) com cor primária
- Título bold (neutral-800)
- Descrição menor (neutral-600)
- Hover: elevação (translateY -4px) + sombra aumentada

---

### 4. Seção de Diferenciais / Por Que Nos Escolher

**Título:** "Por Que Escolher Nosso Serviço?"

**Layout:** 3 colunas (ícone + título + descrição)

| Diferencial | Ícone | Descrição |
|-------------|-------|-----------|
| Orçamento Gratuito | 📋 `ClipboardCheck` | "Avaliação sem compromisso na sua residência" |
| Atendimento Rápido | ⏱️ `Clock` | "Resposta em até 30 minutos pelo WhatsApp" |
| Garantia de Serviço | ✅ `ShieldCheck` | "90 dias de garantia em todos os serviços" |
| Profissional Qualificado | 🎓 `Award` | "Técnico certificado com anos de experiência" |

---

### 5. Seção de Depoimentos (Social Proof)

**Título:** "O Que Nossos Clientes Dizem"

**Layout:** Carrossel horizontal (mobile) / 3 cards visíveis (desktop)

**Estrutura do Card:**
```
⭐⭐⭐⭐⭐

"Depoimento do cliente aqui..."

— Nome do Cliente
   Bairro, Rio Claro
```

**Depoimentos Sugeridos (placeholder):**
1. "Serviço rápido e muito profissional. Resolveu o problema da minha instalação no mesmo dia!"
2. "Orçamento justo e trabalho impecável. Recomendo para toda Rio Claro!"
3. "Atendimento excelente pelo WhatsApp, muito atencioso e pontual."

---

### 6. Seção CTA Final (Conversão)

**Background:** Gradiente azul primário ou imagem com overlay

**Conteúdo Centralizado:**
```
TÍTULO: "Precisa de um Eletricista Agora?"

SUBTÍTULO: "Entre em contato e receba seu orçamento em minutos!"

[BOTÃO WHATSAPP GRANDE]

Texto de urgência: "Atendimento disponível hoje!"
```

**Botão:**
- Tamanho extra grande
- Branco com texto verde ou verde com texto branco
- Ícone WhatsApp animado
- Sombra glow intensa

---

### 7. Footer (Rodapé)

**Background:** neutral-900 (escuro)
**Texto:** neutral-300 / branco

**Layout:** 3 colunas (desktop) / Stack vertical (mobile)

| Coluna 1 - Localização | Coluna 2 - Horário | Coluna 3 - Contato |
|------------------------|--------------------|--------------------|
| **📍 Localização** | **🕐 Horário** | **📞 Contato** |
| Rio Claro – São Paulo | Segunda a Domingo | WhatsApp: (19) XXXXX-XXXX |
| Atendemos toda a cidade | 08:00 às 20:00 | Telefone: (19) XXXXX-XXXX |
| | Conforme disponibilidade | Email: contato@email.com |

**Linha Inferior:**
```
© 2025 Eletricista Residencial Rio Claro. Todos os direitos reservados.
```

---

## 🔘 Botão Flutuante WhatsApp

**Posição:** Canto inferior direito (fixed)
**Estilo:**
- Círculo 60px
- Verde WhatsApp
- Ícone branco centralizado
- Sombra glow pulsante
- Z-index máximo

**Comportamento:**
- Sempre visível
- Hover: scale(1.1) + sombra intensificada
- Click: abre WhatsApp com mensagem pré-definida

**Mensagem Pré-definida:**
```
Olá! Vim pelo site e gostaria de solicitar um orçamento para serviços elétricos.
```

---

## 📱 Responsividade (Mobile-First)

### Breakpoints
```css
/* Mobile First */
@media (min-width: 640px)  { /* sm - Tablets pequenos */ }
@media (min-width: 768px)  { /* md - Tablets */ }
@media (min-width: 1024px) { /* lg - Desktop */ }
@media (min-width: 1280px) { /* xl - Desktop grande */ }
```

### Adaptações Mobile
- Header: Menu hambúrguer com overlay fullscreen
- Hero: Texto centralizado, botões empilhados
- Grids: 1 coluna (mobile) → 2 colunas (tablet) → 3-4 colunas (desktop)
- Font sizes: Reduzidos em 20-30% no mobile
- Padding: Reduzido para 1rem-1.5rem
- Botão flutuante: Menor (50px) no mobile

---

## 🔍 SEO e Meta Tags

```html
<title>Eletricista Residencial Rio Claro SP | Instalações e Reparos Elétricos</title>

<meta name="description" content="Eletricista profissional em Rio Claro - SP. Instalações, reparos e manutenções elétricas residenciais com garantia. Orçamento grátis pelo WhatsApp!">

<meta name="keywords" content="eletricista rio claro, eletricista residencial, instalação elétrica, reparo elétrico, manutenção elétrica, rio claro sp">

<meta property="og:title" content="Eletricista Residencial Rio Claro - SP">
<meta property="og:description" content="Soluções elétricas profissionais para sua residência. Orçamento gratuito!">
<meta property="og:type" content="website">
<meta property="og:image" content="[URL da imagem de compartilhamento]">

<link rel="canonical" href="https://[dominio-do-cliente].com.br">
```

---

## ⚡ Performance e Otimizações

### Checklist Obrigatório
- [ ] Imagens em formato WebP com fallback JPG
- [ ] Lazy loading em imagens abaixo do fold
- [ ] CSS crítico inline no `<head>`
- [ ] Fontes com `display: swap`
- [ ] Minificação de HTML, CSS e JS
- [ ] Compressão Gzip/Brotli no servidor

### Lighthouse Targets
- Performance: > 90
- Accessibility: > 95
- Best Practices: > 90
- SEO: 100

---

## 🛠️ Stack Tecnológica Recomendada

### Opção 1: HTML + Tailwind CSS (Recomendado para simplicidade)
```
- HTML5 semântico
- Tailwind CSS via CDN
- Alpine.js para interatividade (menu mobile, carrossel)
- Lucide Icons ou Font Awesome
```

### Opção 2: Next.js (Para projetos escaláveis)
```
- Next.js 14+ com App Router
- Tailwind CSS
- Framer Motion para animações
- Lucide React para ícones
```

---

## 📦 Entregáveis Esperados

1. **Código fonte completo** (HTML/CSS/JS ou componentes React)
2. **Assets organizados** (ícones, imagens placeholder)
3. **Responsividade testada** em 320px, 768px, 1024px, 1440px
4. **Links funcionais** para WhatsApp com mensagem pré-definida
5. **Animações suaves** sem comprometer performance

---

## 🎯 Critérios de Sucesso

| Critério | Requisito |
|----------|-----------|
| Visual | Design premium, minimalista e profissional |
| Conversão | CTAs claros e destacados, WhatsApp sempre visível |
| Performance | Carregamento < 3 segundos em 3G |
| Mobile | Experiência impecável em smartphones |
| Acessibilidade | Contraste adequado, navegação por teclado |

---

> **Nota para a IA executor:** Priorize a experiência mobile e a conversão via WhatsApp. Cada pixel deve comunicar profissionalismo e confiança. O objetivo final é que o visitante clique no botão do WhatsApp em menos de 10 segundos após entrar na página.
