<?php
	include('/Users/hugo/www/bibhtmler/bibhtmler.php');
	$bibhtmler = new bibhtmler(array('groupby' => 'year'));
?>
<?php echo($bibhtmler->process('/Users/hugo/references/hugomyown.bib')) ?>