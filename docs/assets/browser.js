
(function(){
  const input = document.getElementById('geneSearchInput');
  const out = document.getElementById('geneSearchResults');
  if(!input || !out) return;
  fetch('data/gene_index_v5_clean.json').then(r=>r.json()).then(rows=>{
    function render(q){
      q = q.trim().toUpperCase();
      if(!q){ out.innerHTML='<p class="muted">Type a gene symbol, for example ABCA4, GSDME, DMD, BRCA1, or HTT.</p>'; return; }
      const hits = rows.filter(r => (r.gene_symbol||'').toUpperCase().includes(q)).slice(0,50);
      if(!hits.length){ out.innerHTML='<p class="muted">No matching gene symbol in the all-mapped index.</p>'; return; }
      out.innerHTML = hits.map(r => `<div class="result-row"><strong><a href="${r.detail_page}">${r.gene_symbol}</a></strong><span>${r.public_label_v5}</span><span>${r.ClinVar_PL_record_count} records</span></div>`).join('');
    }
    input.addEventListener('input', ()=>render(input.value));
    render('');
  });
})();
