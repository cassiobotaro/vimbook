Métodos de dobras
------------------

O Vim tem seis modos *fold*, são eles:

- Sintaxe (*syntax*)
- Identação (*indent*)
- Marcas (*marker*)
- Manual (*manual*)
- Diferenças (*diff*)
- Expressões Regulares (*expr*)

Para determinar o tipo de dobra faça
```
:set foldmethod=tipo
```
onde o tipo pode ser um dos tipos listados acima, exemplo:
```
:set foldmethod=marker
```
Outro modo para determinar o método de dobra seria colocando na última
linha do seu arquivo algo assim:
```
vim:fdm=marker:fdl=0:
```

Obs: `fdm` significa *foldmethod*, e `fdl` significa
*foldlevel*. Deve haver um espaço entre a palavra inicial
“vim” e o começo da linha este recurso chama-se *modeline*,
leia mais na seção [modelines](../capitulo_2/modelines.md).
