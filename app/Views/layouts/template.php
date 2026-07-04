<?= $this->include('layouts/header') ?>

<?= $this->include('layouts/sidebar') ?>

<div class="content-wrapper">

    <section class="content-header">

        <div class="container-fluid">

            <div class="row mb-2">

                <div class="col-sm-12">

                    <h1>

                        <?= $title ?? "Machine Learning Prediction Platform" ?>

                    </h1>

                </div>

            </div>

        </div>

    </section>

    <section class="content">

        <div class="container-fluid">

            <?= $this->renderSection('content') ?>

        </div>

    </section>

</div>

<?= $this->include('layouts/footer') ?>