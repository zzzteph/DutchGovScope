---
layout: dutchgov
title: Dutch Government
permalink: /dutchgov/
pagination: 
  enabled: true
  category: dutchgov
  permalink: /:num/
---





<h2 id="key-statistics">Key Statistics</h2>

<h3>Total number of domains: {{paginator.total_posts}}</h1>
<h3 id="ssl-grades">SSL Grades</h3>
<p>Analysys and grade statistics of SSL configuration with <a href="https://www.ssllabs.com/ssltest/">https://www.ssllabs.com/ssltest/</a>

<ul>
  <li>
<strong>HttpOnly (1392):</strong> Helps mitigate the risk of client-side script accessing the protected cookie.</li>
  <li>
    <li>
<strong>HttpOnly (1392):</strong> Helps mitigate the risk of client-side script accessing the protected cookie.</li>
  <li>
    <li>
<strong>HttpOnly (1392):</strong> Helps mitigate the risk of client-side script accessing the protected cookie.</li>
  <li>
  
</ul>  


</p>

<h3 id="cookies-security-flags">Cookies Security Flags</h3>
<p>Cookies play a crucial role in web security and with special flag attributes security could enhance cookie of customers very much:</p>
<ul>
  <li>
<strong>HttpOnly (1392):</strong> Helps mitigate the risk of client-side script accessing the protected cookie.</li>
  <li>
<strong>Secure (1398):</strong> Ensures cookies are sent over secure, HTTPS connections.**</li>
  <li>
<strong>Same-Site (24):</strong> Prevents the browser from sending this cookie along with cross-site requests.</li>
</ul>

<h3 id="top-5-server-headers">Top 5 server headers</h3>
<ul>
  <li>nginx - <strong>3080</strong>
</li>
  <li>Microsoft-IIS/10.0 - <strong>984</strong>
</li>
  <li>Apache - <strong>861</strong>
</li>
  <li>BigIP - <strong>151</strong>
</li>
  <li>Microsoft-HTTPAPI/2.0 - <strong>134</strong>
</li>
  <li>Apache/2 - <strong>119</strong>
</li>
</ul>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>SSL Rank</th>
            <th>HTTP Rank</th>
            <th>Alive subdomains :page_facing_up:</th>
            <th>All subdomains :page_facing_up:</th>
            <th>URL's :page_facing_up:</th>
        </tr>
     </thead>
<tbody>
{% for post in paginator.posts %}
<tr>
    <td><a href="{{ post.internal_url }}">{{ post.title }}</a></td>
    <td><a href="{{ post.internal_url }}">{{ post.ssl_rank }}</a></td>
    <td><a href="{{ post.internal_url }}">{{ post.http_rank }}</a></td>
    <td><a href="{{ post.subdomains_link }}">{{ post.subdomains_count }}</a></td>
    <td><a href="{{ post.all_subdomains_link }}">{{ post.all_subdomains_count }}</a></td>
    <td><a href="{{ post.url_link }}">{{ post.urls_count }}</a></td>
</tr>

{% endfor %}
</tbody>

</table>




<!-- Pagination links -->
<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path }}" class="previous">
      Previous
    </a>
  {% else %}
    <span class="previous">Previous</span>
  {% endif %}
  <span class="page_number ">
    Page: {{ paginator.page }} of {{ paginator.total_pages }}
  </span>
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path }}" class="next">Next</a>
  {% else %}
    <span class="next ">Next</span>
  {% endif %}
</div>